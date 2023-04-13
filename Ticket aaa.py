class Ticket:
    ticket_counter = 2000

    def __init__(self, staff_id, creator_name, contact_email, issue_description):
        self.ticket_number = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.issue_description = issue_description
        self.response = "Not Yet Provided"
        self.status = "Open"

        if "Password Change" in self.issue_description:
            self.resolve_password_change()

    def resolve(self, response):
        self.response = response
        self.status = "Closed"

    def reopen(self):
        self.status = "Reopened"

    def provide_response(self, response):
        self.response = response

    def resolve_password_change(self):
        new_password = self.staff_id[:2] + self.creator_name[:3]
        self.response = f"New password generated: {new_password}"
        self.status = "Closed"

    @staticmethod
    def print_ticket_info(tickets):
        for ticket in tickets:
            print(f"Ticket Number: {ticket.ticket_number}")
            print(f"Name: {ticket.creator_name}")
            print(f"Staff ID: {ticket.staff_id}")
            print(f"Email: {ticket.contact_email}")
            print(f"Issue: {ticket.issue_description}")
            print(f"Response: {ticket.response}")
            print(f"Status: {ticket.status}\n")

    @staticmethod
    def print_ticket_stats(tickets):
        submitted = len(tickets)
        resolved = sum(1 for ticket in tickets if ticket.status == "Closed")
        open_tickets = sum(1 for ticket in tickets if ticket.status in ["Open", "Reopened"])
        print(f"Number of Submitted Tickets: {submitted}")
        print(f"Number of Resolved Tickets: {resolved}")
        print(f"Number of Open Tickets: {open_tickets}\n")