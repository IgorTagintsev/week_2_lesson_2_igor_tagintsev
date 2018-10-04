def sort_members_by_name_length(list_of_members: list):
    list_of_members.sort(key=lambda member: member['age'])
    return sorted(list_of_members, key=lambda member: len(member['name']))


