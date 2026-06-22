# set

responses = ["yes", "no", "yes", "maybe", "no", "yes"]
unique_responses = set(responses)

print(
    "yes" in unique_responses, "always" in unique_responses, "maybe" in unique_responses
)


numbers = [4, 4, 2, 2, 4]
unique_numbers = set(numbers)
print(unique_numbers)


group_a = {"alice", "bob", "carol"}
group_b = {"bob", "dave"}
group_c = {"carol", "eve"}

merged = group_a.union(group_b)
merged = merged.union(group_c)

print(merged)


survey_a = ["blue", "green", "blue", "red", "green"]
survey_b = ["yellow", "blue", "yellow", "red"]

clean_a = set(survey_a)
clean_b = set(survey_b)

all_unique = clean_a.union(clean_b)
print(all_unique)
