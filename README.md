# Movie Review System


This is a **Django-based Movie Review System** where users can browse movie details, read reviews, and submit their own reviews.

### ⭐ Features
- **View Movie Details:** Users can see movie names, directors, genres, and more.  
- **Read Reviews Without Login:** Anyone can read existing reviews.  
- **Submit Reviews (Login Required):** Users must log in to submit a review.  
- **Review Submission Feedback:** Success and error messages appear when submitting a review.  

### 🔹 Review Submission Behavior
- Users can write a review with a **username, rating (1-5), and review text**.
- If a review is successfully submitted, a **green success message** appears.
- If the form is incomplete, a **red error message** appears.

### ⚙️ How It Works
1. **Submitting a Review**
   - A user enters a username.
   - A rating (1-5) and review text are required.
   - The system validates input and saves the review.

2. **Displaying Messages**
   - **Success message:** "Review submitted successfully!"
   - **Error message:** "Review submission failed. Please fill all fields."

3. **Reading Reviews**
   - Existing reviews appear below the movie details.
   - Each review shows **username, rating, and review text**.


### 🛠 Technologies Used
- **Django** (Backend)
- **HTML, CSS, JavaScript** (Frontend)
- **Bootstrap 5** (UI Styling)
- **PostgreSQL** (Database)

