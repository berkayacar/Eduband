#  Deployment Plan – EduBand

---

##  Backend Setup
- **Flask application** containerized with Docker  
- Local deployment managed using:
  - `docker-compose.yml` for service orchestration  
  - `Dockerfile` including production-ready server setup with **Gunicorn** and **Flask-CORS** configuration  
- **SQLite** database used for lightweight and portable development

---

## Mobile App (Future Plan)
- Mobile application planned with **React Native**
- Communication with Flask backend through secure **REST API** endpoints

---

## Environment Variables
- API keys, database URLs, and secret configurations managed via `.env` file  
- Environment variables injected into Docker containers during build and runtime



## Testing
- **API endpoints** tested with Postman  
- **Sensor data** simulated for backend validation  
- **Device connection** tested using Bluetooth debugging on real Android devices



## Production Notes
- Although EduBand is currently a **project prototype**, the backend system is designed to be deployed to:
  - **Render** (for backend hosting)
  - **Railway.app** (alternative backend hosting)
  - **Vercel** or **Netlify** (for future frontend hosting, if needed)
- Potential integration with **cloud-based SQLite alternatives** or **lightweight managed databases** for scaling



##  Challenges
- Local **port conflicts** solved by customizing Flask server ports through `.env` file  
- Bluetooth pairing inconsistencies during mobile testing were resolved by **switching to real devices** instead of emulators  
- SQLite concurrency issues addressed by adding **proper locking** and **retry logic** during read/write operations


