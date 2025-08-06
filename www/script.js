// Set current year in footer
document.getElementById('currentYear').textContent = new Date().getFullYear();

// Navigation functionality
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    
    // Remove active class from all nav links and sections
    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
    document.querySelectorAll('.content-section').forEach(s => s.classList.remove('active'));
    
    // Add active class to clicked link
    this.classList.add('active');
    
    // Show corresponding section
    const sectionId = this.getAttribute('data-section');
    document.getElementById(sectionId).classList.add('active');
  });
});

// Blog functionality
function showFullPost(postId) {
  // Hide blog list
  document.getElementById('blog-list').style.display = 'none';
  
  // Show full post
  document.getElementById(`full-post-${postId}`).classList.add('active');
}

function showBlogList() {
  // Hide all full posts
  document.querySelectorAll('.full-post').forEach(post => {
    post.classList.remove('active');
  });
  
  // Show blog list
  document.getElementById('blog-list').style.display = 'block';
} 