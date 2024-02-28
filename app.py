


import streamlit as st

class Candidate:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.votes = 0

    def add_vote(self):
        self.votes += 1

class Election:
    def __init__(self):
        self.candidates = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def vote(self, candidate_index):
        if 0 <= candidate_index < len(self.candidates):
            self.candidates[candidate_index].add_vote()
            st.success("Vote cast successfully!")
        else:
            st.error("Invalid candidate index.")

    def get_results(self):
        results = []
        for candidate in self.candidates:
            results.append((candidate.name, candidate.party, candidate.votes))
        return results

def home(election):
    st.header("Register Candidates")
    name = st.text_input("Enter Candidate Name")
    party = st.text_input("Enter Party Name")
    if st.button("Register Candidate"):
        if not name or not party:
            st.error("Candidate Name and Party Name cannot be empty.")
        else:
            candidate = Candidate(name, party)
            election.add_candidate(candidate)
            st.success("Candidate registered successfully!")

    st.header("Cast Vote")
    if not election.candidates:
        st.warning("No candidates registered. Please register candidates before voting.")
    else:
        vote_options = [candidate.name for candidate in election.candidates]
        vote_index = st.selectbox("Select Candidate to Vote", vote_options)
        if st.button("Cast Vote"):
            election.vote(vote_options.index(vote_index))

    st.header("Election Results")
    results = election.get_results()
    for name, party, votes in results:
        st.write(f"**Name:** {name}, **Party:** {party}, **Votes:** {votes}")

def about():
    st.title("📄 About")
    st.write(
        "BANO QABIL is an online election system developed with Streamlit, allowing users to:"
        "\n\n1. **Register Candidates:** Easily register candidates by providing their names and party affiliations."
        "\n2. **Cast Votes:** Simple and intuitive interface for casting votes, promoting user engagement."
        "\n3. **View Results:** Real-time access to election results, ensuring transparency and accessibility."
        "\n\nThe system works by creating instances of Candidate and Election classes. Candidates can be registered, and users can cast votes for registered candidates. The system keeps track of the votes and displays real-time election results."
        "\n\nDesigned to streamline online elections, BANO QABIL aims to make the process efficient and user-friendly."
    )

def contact_us():
    st.title("📧 Contact Us")
    st.write("For inquiries, please contact us at: example@example.com")
    # Add more contact information.

def main():
    st.title("BANO QABIL - Online Election System")

    election = Election()  # Move election instance outside main() to persist data between function calls

    menu = ["Home", "About", "Contact Us"]
    st.sidebar.title("Menu")
    choice = st.sidebar.radio("Select Option", menu)

    if choice == "Home":
        home(election)
    elif choice == "About":
        about()
    elif choice == "Contact Us":
        contact_us()

if __name__ == "__main__":
    main()