# Django Blog Website

A simple and dynamic Django-based Blog Website where users can create, read, update, and delete blog posts. The project follows an MVC (Model-View-Template) structure and includes user authentication features such as login, registration, and logout.

## Features

### 🔐 User Authentication
- **User Registration**: New users can create accounts with username, email, and password
- **User Login/Logout**: Secure authentication system
- **User Profile**: Personal profile page showing user information

### 📝 Blog Post Management (CRUD Operations)
- **Create Posts**: Authenticated users can create new blog posts
- **Read Posts**: Anyone can view blog posts and browse them
- **Update Posts**: Post authors can edit their own posts
- **Delete Posts**: Post authors can delete their own posts

### 🎨 User Interface
- **Responsive Design**: Bootstrap-powered responsive UI
- **Clean Layout**: Professional blog layout with navigation and sidebar
- **Post Listing**: Home page shows all posts with pagination
- **User-specific Posts**: View posts by specific authors
- **Post Details**: Full post view with author information and timestamps

### 🔒 Security Features
- **CSRF Protection**: All forms include CSRF tokens
- **User Authorization**: Only post authors can edit/delete their posts
- **Login Required**: Creating posts requires authentication
- **Form Validation**: Proper form validation for all inputs

## Screenshots

### Home Page
![Home Page](https://github.com/user-attachments/assets/13dd98a3-4e12-4bbb-a6fe-127813724846)

### User Registration
![Registration Page](https://github.com/user-attachments/assets/0761f6d1-2c6a-4ce4-9012-198280fb0507)

### Blog Post Detail
![Blog Post Detail](https://github.com/user-attachments/assets/7691d8d7-45a2-48bd-868c-2e4e8dc83fed)

### Home Page with Posts
![Home with Posts](https://github.com/user-attachments/assets/2da505c3-a4b8-430a-ab85-80089be21ad7)

## Project Structure

```
Blog-Website/
├── blog_website/          # Main Django project
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL configuration
│   └── ...
├── blog/                 # Blog application
│   ├── models.py         # Post model
│   ├── views.py          # Blog views (CRUD operations)
│   ├── urls.py           # Blog URL patterns
│   ├── forms.py          # Custom forms
│   ├── admin.py          # Admin configuration
│   └── tests.py          # Test cases
├── users/                # User authentication app
│   ├── views.py          # User auth views
│   └── ...
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── blog/             # Blog templates
│   └── users/            # User auth templates
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Installation and Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/pappukumar35/Blog-Website.git
   cd Blog-Website
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Register a new account or login
   - Start creating blog posts!

## Usage

### For Regular Users
1. **Register**: Create a new account on the registration page
2. **Login**: Sign in with your credentials
3. **Create Posts**: Click "New Post" to create blog posts
4. **View Posts**: Browse all posts on the home page
5. **Manage Posts**: Edit or delete your own posts from the post detail page
6. **Profile**: View your profile and all your posts

### For Administrators
- Access the Django admin panel at `/admin/` to manage users and posts
- Use the admin interface for advanced post and user management

## Testing

Run the test suite to ensure everything is working correctly:

```bash
python manage.py test
```

The test suite includes:
- User authentication tests
- Post CRUD operation tests
- Authorization and permission tests
- Form validation tests

## Technologies Used

- **Backend**: Django 5.2.6
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Authentication**: Django's built-in authentication system
- **Styling**: Bootstrap for responsive design

## Key Django Concepts Demonstrated

- **Models**: Post model with relationships to User
- **Views**: Class-based views (ListView, DetailView, CreateView, UpdateView, DeleteView)
- **Templates**: Template inheritance and context variables
- **Forms**: Custom forms with validation
- **URLs**: URL routing and patterns
- **Authentication**: Login required decorators and user permissions
- **Admin**: Custom admin interface
- **Testing**: Unit tests for models and views

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Add tests for your changes
5. Ensure all tests pass (`python manage.py test`)
6. Commit your changes (`git commit -am 'Add new feature'`)
7. Push to the branch (`git push origin feature/new-feature`)
8. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

- Add comment system for blog posts
- Implement post categories and tags
- Add search functionality
- Include image upload for posts
- Add email verification for user registration
- Implement password reset functionality
- Add social media sharing buttons
- Create REST API endpoints
