import streamlit as st
import pickle

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()
def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History):
	if Gender == "Male":
		Gender = 0
	else:
		Gender = 1

	if Married == "Unmarried":
		Married = 0
	else:
		Married = 1

	if Credit_History == "Unclear Debts":
		Credit_History = 0
	else:
		Credit_History = 1

	LoanAmount = LoanAmount / 1000

	# Making predictions
	prediction = classifier.predict(
		[[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

	if prediction == 0:
		pred = 'Rejected'
	else:
		pred = 'Approved'
	return pred

def main():
	# title
	st.title("Checking Loan Eligibility")

	#select box & inputs
	Gender = st.selectbox('Gender', ("Male", "Female"))
	Married = st.selectbox('Marital Status', ("Unmarried", "Married"))
	ApplicantIncome = st.number_input("Applicants monthly income")
	LoanAmount = st.number_input("Total loan amount")
	Credit_History = st.selectbox('Credit_History', ("Unclear Debts", "clear Debts"))
	result = ""

    #result
	if st.button("Predict"):
		result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History)
		if result=="Approved":
		    st.success('Your loan is {}'.format(result))
		    st.success('You will repaid {} monthly'.format(0.40*ApplicantIncome))
		if result == "Rejected":
			st.success('Your loan is {}'.format(result))




if __name__ == '__main__':
	main()
