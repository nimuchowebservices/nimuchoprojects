// Custom JavaScript for Nimucho Digital

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    
    // Add loading spinner
    const loader = document.createElement('div');
    loader.className = 'loader';
    loader.innerHTML = '<div class="spinner"></div>';
    document.body.appendChild(loader);
    
    // Hide loader after page loads
    window.addEventListener('load', function() {
        setTimeout(function() {
            loader.classList.add('hide');
            setTimeout(function() {
                loader.remove();
            }, 500);
        }, 500);
    });
    
    // Animate stats when they come into view
    const stats = document.querySelectorAll('.stat-number');
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const stat = entry.target;
                const target = parseInt(stat.innerText);
                let current = 0;
                const increment = target / 50;
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        stat.innerText = target + '+';
                        clearInterval(timer);
                    } else {
                        stat.innerText = Math.floor(current) + '+';
                    }
                }, 20);
                observer.unobserve(stat);
            }
        });
    }, observerOptions);
    
    stats.forEach(stat => observer.observe(stat));
    
    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                // Close mobile menu if open
                const navbarCollapse = document.querySelector('.navbar-collapse');
                if (navbarCollapse.classList.contains('show')) {
                    navbarCollapse.classList.remove('show');
                }
            }
        });
    });
    
    // Navbar background change on scroll
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
        }
    });
    
    // Add active class to nav links on scroll
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
                link.style.color = '#dc2626';
            } else {
                link.style.color = '';
            }
        });
    });
    
    // Form submission handler
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
            submitBtn.disabled = true;
            
            // Simulate form submission (replace with actual AJAX call)
            setTimeout(() => {
                submitBtn.innerHTML = '<i class="fas fa-check"></i> Message Sent!';
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                    this.reset();
                }, 2000);
            }, 1500);
        });
    }
    
    // Parallax effect for hero section
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero');
        if (hero) {
            hero.style.backgroundPositionY = `${scrolled * 0.5}px`;
        }
    });
    
    // Add tooltips to social icons
    const socialIcons = document.querySelectorAll('.social-icons a');
    socialIcons.forEach(icon => {
        icon.setAttribute('target', '_blank');
        icon.setAttribute('rel', 'noopener noreferrer');
    });
    
    // Lazy load images
    const images = document.querySelectorAll('img');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.style.opacity = '0';
                img.addEventListener('load', () => {
                    img.style.transition = 'opacity 0.5s';
                    img.style.opacity = '1';
                });
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
    
    // Add year to copyright
    const copyright = document.querySelector('.footer .text-center p');
    if (copyright) {
        const year = new Date().getFullYear();
        copyright.innerHTML = copyright.innerHTML.replace('2026', year);
    }
});

// Add CSS for active nav link
const style = document.createElement('style');
style.textContent = `
    .navbar-nav .nav-link.active {
        color: #dc2626 !important;
        font-weight: 600;
    }
    .navbar-nav .nav-link.active::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 50%;
        transform: translateX(-50%);
        width: 30px;
        height: 2px;
        background: #dc2626;
    }
    .navbar-nav .nav-link {
        position: relative;
    }
`;
document.head.appendChild(style);