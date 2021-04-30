from collections import defaultdict
import pandas

#1) Read the CSV file
raw_survey = pandas.read_csv("real_survey.csv", index_col=0, header = None)
# Read the survey as a table
survey = [list(row) for row in raw_survey.values]

#2) Iterate through the survey
def user_responses(user):
  # create temporary dictionary that defaults as a list
  answer_values = defaultdict(list)
  # iterate through each answer a user gave. Enumerate gives us an index
  # which we extract to the numeric value of the answer (-4...4) later
  for index, value in enumerate(user):
    # see if it's an integer
    if isinstance(value, int):
      # scale the answer depending on the survey... in this case subtract 4 (survey answers must range from -x to +x). 
      answer_values[value] = index - 4
    else:
      # if the response is a string, remove the comma and turn it into a list
      temp = value.split(", ")
      for i in temp:        
          # now that it's a list, scale and append to the answer_values list
        answer_values[int(i)] = index - 4
    # return so next iterations don't overwrite data
  return dict(answer_values)

#3) Convert the users answers to its own dictionary of lists
def convert_table(survey_results):
  parsed_survey = []
  # iterate through each user's responses
  for user in survey_results:
    parsed_survey.append(user_responses(user))
  # return the dictionary as a dictionary, not a defaultdict
  return parsed_survey

# sort the dictionary into a table
sorted_table = convert_table(survey)

# turn the table into a dataframe using pandas, which is a way to render CSVs
dataframe = pandas.DataFrame(sorted_table)
# organize the CSV so the columns are in ascending order
dataframe = dataframe.reindex(sorted(dataframe.columns), axis = 1)

# save it to a new CSV file
dataframe.to_csv("FORMAT_SURVEY.csv")

# add a header to the survey:


# notify upon completion
print ("All Done! :)")