# import the installed Jira library
from jira import JIRA



# region CONFIG
# Specify a server key.
jiraOptions = {'server': "https://pcdd.atlassian.net"}

# Get a JIRA client instance, pass, Authentication parameters and the Server name.
jira = JIRA (
	options = jiraOptions, 
    basic_auth = (
	    "phandanh2112@gmail.com", 
	    "ATATT3xFfGF0-F2D-Zldo1RzFvGhZer0x-jrmTlCtxLxU5KCNW1FYpC4WpdsdR-xpXRVw4nkBOF8XPnPfyww698XJjT8E5HM--xlHHXEPoJ99OMztkr-zy8RTcDn-JgEN-opF6_yJg10MCInquQR6yKgzqRFSTT0dDglX9WZrkTnfTKCnMA7Dnc=99CE2D11"
	)
)

project_assignment = 'project = Py_fetch_Jira'
# endregion



print("login...\n")

while 1:
    print("----------------------------------------------------------------")
    print("1. My ticket.")
    print("2. Ticket details.")
    print("3. Exit.")

    opt = input("Select action (1 or 2, ..): ")

    subTasks = []

    match opt:
        case "1":
            print("My ticket:")
            # Search all issues mentioned against a PROJECT NAME.
            for singleIssue in jira.search_issues(jql_str = project_assignment):
                print(singleIssue.key + ":")                                        # ticket ID
                print("\tSummary:", singleIssue.fields.summary)
                print("\tStatus:", singleIssue.fields.status)
        case "2":
            ticketID = input("Ticket ID: ")
            print(ticketID + ":")

            singleIssue = jira.issue(ticketID)
            print("\tSummary:", singleIssue.fields.summary)
            print("\tStatus:", singleIssue.fields.status)
            print("\tDescription:")
            print("\t\t" + singleIssue.fields.description)

            for singleSubTask in jira.search_issues("parent = %s" % singleIssue):
                subTasks.append(singleSubTask.key)
            print("\tSubtasks:", subTasks)

            print("\tOriginal Estimate:", singleIssue.fields.timetracking.raw['originalEstimate'] + ',', 
                  "Remaining Estimate:", singleIssue.fields.timetracking.remainingEstimate + ',', 
                  "Time spent:", singleIssue.fields.timetracking.raw['timeSpent'])
        case "3":
            print("Exiting...")
            break
    
    print("----------------------------------------------------------------\n")