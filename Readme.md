# PROBLEM 4
## Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. 
We can construct this hierarchy as such. Where User is represented by str representing their ids. 
Example :
<br>If parent consist a subgroup Child
<br>If Child Consist a subgroup Subchild
<br>If Subchild consist a user Subchild-user
<br>Then if we check that subchild-user is in group Parent it should return True
<br>
### Algorithm:
1. if user is in current group then return true
2. else if current group have no subgroups return false
3. else if current group have subgroup then recursively iterate through each each subgroup to
search for user.


### Time Complexity Analysis:
• is_user_in_group: O(B*D)<br>
◦ where B=Max Number of Subgroups in a Group(Branching Factor)<br>
◦ where D=Max Depth of Subgroup(Depth)<br>


### Space Complexity Analysis:
• is_user_in_group: O(B*D)
◦ where B=Max Number of Subgroups in a Group(Branching Factor)<br>
◦ where D=Max Depth of Subgroup(Depth)<br>
