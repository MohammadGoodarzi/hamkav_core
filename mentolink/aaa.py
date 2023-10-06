
def authenticate(self, request: HttpRequest) -> Optional[User]:
auth = get_authorization_header(request).split()
if not auth or auth[0].lower() != self.keyword.lower().encode():
return None

if len(auth) == 1:
msg = _("Invalid Authorization header. No credentials provided.")
raise exceptions.AuthenticationFailed(msg)
elif len(auth) > 2:
msg = _(
"Invalid Authorization header. Credentials string "
"should not contain spaces."
)
raise exceptions.AuthenticationFailed(msg)

try:
raw_token = auth[1].decode()
validated_token = self.get_validated_token(raw_token)
except TokenError as e: # <-- add this line
raise exceptions.AuthenticationFailed(e.args[0]) # <-- add this line
except UnicodeError:
msg = _(
"Invalid Authorization header. Credentials not correctly base64 encoded."
)
raise exceptions.AuthenticationFailed(msg)

return self.get_user(validated_token)

This will catch the TokenError exception and raise an AuthenticationFailed exception with the appropriate message, such as "Token is invalid or expired". You can find more details and explanations of this issue and solution in this web page: 1https://stackoverflow.com/questions/64047332/django-expire-token-authentication. I hope this helps you with your task. blush
https://stackoverflow.com/questions/64047332/django-expire-token-authentication

10:22 PM
how to write custom token validation in ninja-jwt

Bing, 10:23 PM
To write custom token validation in ninja-jwt, you need to create a custom validator class that implements the ITokenValidator interface. The ITokenValidator interface has a Validate method that takes a JwtSecurityToken as a parameter and returns a boolean value indicating whether the token is valid or not. You can use the JJWT library to parse and verify the token, and add your own logic to check the claims or other fields in the token. For example, you can create a custom validator class like this:

using System.IdentityModel.Tokens.Jwt;
using Ninja.Jwt;
using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.Security;

public class CustomTokenValidator : ITokenValidator
{
private readonly string _secretKey;

public CustomTokenValidator(string secretKey)
{
_secretKey = secretKey;
}

public bool Validate(JwtSecurityToken token)
{
// Parse the token using JJWT
var parser = new JwtParserBuilder()
.SetSigningKey(GetPublicKey(_secretKey))
.Build();

var jwt = parser.ParseClaimsJws(token.RawData);

// Check the claims or other fields in the token
var claims = jwt.Body;
var issuer = claims.Issuer;
var audience = claims.Audience;
var expiration = claims.Expiration;

// Add your own validation logic here
// For example, check if the issuer is valid
if (issuer != "https://example.com")
{
return false;
}

// Return true if the token is valid, false otherwise
return true;
}

private RsaKeyParameters GetPublicKey(string key)
{
// Convert the base64 encoded key to a byte array
var keyBytes = Convert.FromBase64Stringkey;

// Create an asymmetric key parameter from the key bytes
var asymmetricKeyParameter = PublicKeyFactory.CreateKey(keyBytes);

// Cast the key parameter to a RSA key parameter
var rsaKeyParameters = (RsaKeyParameters)asymmetricKeyParameter;

return rsaKeyParameters;
}
}

Then, you can register your custom validator class in the Startup.cs file like this:

using Ninja.Jwt;

public class Startup
{
public void ConfigureServices(IServiceCollection services)
{
// Add your secret key here
var secretKey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzay8...";

// Register your custom validator class as a singleton service
services.AddSingleton<ITokenValidator>(new CustomTokenValidator(secretKey));

// Add other services here
}
}
