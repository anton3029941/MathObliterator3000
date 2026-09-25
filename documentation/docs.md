### The goal
A web application that receives a photo, transcribes mathematical formulas into LaTeX code, and sends back a solution.

### Requirements
Users can send an image file
The solution is written in LaTeX code
The app is expected to sustain at least one user

### Out of scope for V1
User accounts
Histories of past calculations
Problems beyond SymPy's capabilities

### Data Flow
HTML form accepts an image and sends it to the server. Then the server analyses it, calculates and returns a solution.
Doesn't require a database.

### Infrastructure
/MathObliterator3000
    /server
        /images
            /...
        /server.py <- entry
        /solve.py
    /website
        /home.html
        /style.css

### Stack
Flask — fits the project scale
Pix2Text — the best free option for a Math OCR
SymPy — free-to-use symbolic maths library

### Consider
DDoS/DoS attacks, image resolution/file size, invalid file extensions