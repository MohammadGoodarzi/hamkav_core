import re



def to_postgres_form():
    # original_query = "select * from tt where name=@name and family = @family"
    # original_query = re.sub(r'\s*=\s*', '=', original_query)
    # pattern = re.compile(r'\b(\w+)=(@\w+)\b')
    # matches = pattern.findall(original_query)
    # print(matches)
    

    # if matches:
    #     for match in matches:
    #         original_part, placeholder_part = match
    #         original_query = original_query.replace("{}={}".format(original_part, placeholder_part),
    #                                                 "%({})s".format(original_part))


    original_query = "select * from tt where name=@name and family=@family"

    # Define a pattern to match @[parameter]
    pattern = re.compile(r'@(\w+)')

    # Find all matches in the original query
    matches = pattern.findall(original_query)

    # Replace each match with the desired format
    reversed_query = pattern.sub(r'%(\1)s', original_query)
    print(reversed_query)
    
    
def from_postgres_form():

    original_query = "select * from tt where %(name)s and %(family)s"
    pattern = re.compile(r'%\((\w+)\)s')
    # Replace each match with the desired format
    matches = pattern.findall(original_query)
    
    converted_query = pattern.sub(r'\1=@\1', original_query)
    
    # match = pattern.match(original_query)
    # print(matches)
    

    # if matches:
    #      for match in matches:
    #         original_part, placeholder_part = match
    #         original_query = original_query.replace("%({})s".format(original_part, placeholder_part),
    #                                                 "{}=@{}".format(original_part))
    #         # placeholder = matches.group(1)
            # converted_string = original_query.replace("%({})s".format(placeholder), "{}=@{}".format(placeholder, placeholder))
    print(converted_query)
    # else:
    #     print("Pattern not found.")


to_postgres_form()
from_postgres_form()
