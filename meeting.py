attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James","Gail"])
optional_invitees = ["Ben","Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "attendees currently.")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("CC: " + cc_line)
