EduBand – System Architecture Design Overview
1. System Overview
EduBand utilizes a device-server architecture, where a wearable device captures focus-related data and communicates with a lightweight backend API.
The backend server, built with Flask and containerized with Docker, manages data storage, report generation, and device synchronization.

The mobile application (currently in the planning phase) will be developed with React Native to enable students to monitor their concentration trends and download performance summaries.
The device connects to mobile devices over Bluetooth for real-time data transfer and feedback.

System Components:

Wearable Device (Focus tracking and vibration feedback)

Flask REST API (Backend server)

React Native Mobile App (Future)

Bluetooth Communication Layer

2. User Interface Approach
The UI of EduBand emphasizes simplicity and ease of use, with an intuitive flow to ensure that students can quickly access key focus metrics without distraction.
Early-stage wireframes were designed using Figma and will be translated into mobile app components using React Native libraries.

Planned Screens:
Sign In / Sign Up: Secure user authentication

Focus Dashboard: Live attention score and activity overview

Device Connection: Bluetooth pairing and monitoring screen

Focus History: Past session summaries and focus trends

Weekly Reports: PDF downloads of weekly performance evaluations

3. Visual Design
Primary Color: #4E73DF (Energetic Blue – inspires focus)

Secondary Color: #FFFFFF (Clean white background for readability)

Font Family: Poppins (Optimized for clarity across mobile devices)

Color and typography choices aim to promote focus while maintaining an aesthetically pleasing user experience.

4. Navigation Strategy
App navigation will be structured with React Navigation:

Stack Navigation for linear flows (Login → Dashboard → Reports)

Tab Navigation for quick switching between major sections (Home, History, Settings)

5. Responsiveness Testing
The user interface design will be validated across multiple platforms and screen sizes, including:

iPhone 13 Pro (iOS Simulator)

Pixel 5 (Android Emulator)

Samsung Galaxy A52 (Real Android Device)

Initial checks for responsiveness on small tablets (iPad Mini, Galaxy Tab A7)
