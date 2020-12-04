Call function databaseAccess to perform queries

Takes 2 arguments, int func and list args
func selects the stored procedure to run

#1 to get the full tallied list of votes args, = none
#2 to check if voter has already voted, args = (eid)
#3 to insert a vote, args = (eid, cid, timestamp)

Args is the list of parameters for the function, leave empty if not needed

