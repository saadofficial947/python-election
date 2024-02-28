
# candidates.py
class Candidate:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.votes = 0

    def add_vote(self):
        self.votes += 1

# election.py
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

import streamlit as st

# Custom CSS for enhanced styling and background animation
st.markdown("""
    <style>
        body {
            background: linear-gradient(90deg, #6495ED, #ADD8E6, #6495ED, #ADD8E6);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }

        @keyframes gradient {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        .sidebar .sidebar-content {
            background-color: #4682B4;  /* Steel Blue */
            color: white;
            padding: 20px;
            border-radius: 10px;
        }
        .css-1p5ro2t {
            background-color: #4682B4;  /* Steel Blue */
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .css-1v3fvcr {
            background-color: #87CEEB;  /* Sky Blue */
            color: black;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px.
        }
        .header-style {
            background-color: #4682B4;  /* Steel Blue */
            color: white;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

def home(election):
    st.header("Register Candidates")
    name = st.text_input("Enter Candidate Name")
    party = st.text_input("Enter Party Name")

    if st.button("Register Candidate", key="register_button"):
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

        if st.button("Cast Vote", key="cast_vote_button"):
            election.vote(vote_options.index(vote_index))

    st.header("Election Results")
    results = election.get_results()
    for name, party, votes in results:
        st.write(f"**Name:** {name}, **Party:** {party}, **Votes:** {votes}")

def about():
    st.title("📄 About")
    st.markdown("BANO QABIL stands as a sophisticated online election system built using Streamlit, offering a robust set of features to ensure a seamless and transparent voting process.")
    
    st.header("1. Candidate Registration")
    st.write("Easily register candidates by entering their names and respective party affiliations. This crucial step maintains a well-organized list of candidates, empowering voters to make informed decisions.")

    st.header("2. Intuitive Voting Interface")
    st.write("The user-friendly interface simplifies the voting process, fostering user engagement. Voters can effortlessly cast their votes for registered candidates, enhancing accessibility and inclusivity in the democratic process.")

    st.header("3. Real-time Results Display")
    st.write("BANO QABIL provides real-time access to election results, ensuring transparency and accessibility. The system employs a dynamic display that updates as votes are cast, enabling stakeholders to stay informed about the evolving electoral landscape.")

    st.write("\nTo achieve these functionalities, BANO QABIL utilizes two essential classes:")
    
    st.subheader("Candidate Class")
    st.write("The `Candidate` class represents an individual running for office. Each candidate is associated with a name, party affiliation, and a count of received votes. The class includes a method to increment the vote count when a vote is cast in their favor.")

    st.subheader("Election Class")
    st.write("The `Election` class manages the overall election process. It keeps track of registered candidates, allows new candidates to be added, enables the casting of votes, and provides a method to retrieve real-time election results. The class ensures the integrity and accuracy of the voting system.")

    st.write("\nBANO QABIL is meticulously crafted to streamline online elections, ensuring efficiency, user-friendliness, and security. The system's architecture allows for easy scalability and adaptation to various election scenarios, making it a robust solution for democratic processes.")
    
    st.write("\nWhether facilitating small-scale local elections or contributing to larger national events, BANO QABIL prioritizes the principles of fairness, accessibility, and transparency, thereby elevating democratic practices to new heights.")

def contact_us():
    st.title("📧 Contact Us")
    st.write("For inquiries, please contact us at: example@example.com")

def main():
    st.title("BANO QABIL - Online Election System")
    st.image(r"C:\\Users\\Muhammad Sajjad\\Downloads\\pexels-element-digital-1550337.jpg", width=200)
    
    election = Election()  # Move election instance outside main() to persist data between function calls

    st.sidebar.title("Menu")
    choice = st.sidebar.radio("Select Option", ["Home", "About", "Contact Us"])

    if choice == "Home":
        home(election)
    elif choice == "About":
        about()
    elif choice == "Contact Us":
        contact_us()

if __name__ == "__main__":
    main()
