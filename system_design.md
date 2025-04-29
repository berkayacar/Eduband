#  EduBand – System Architecture Design Overview

---

## **1. System Overview**

EduBand utilizes a **device-server architecture**, where a wearable device captures focus-related data and communicates with a lightweight backend API.

The backend server, built with **Flask** and containerized with **Docker**, manages:

- Data storage  
- Report generation  
- Device synchronization  

 **Mobile Application** (planned with **React Native**) will allow students to:

- Monitor concentration trends  
- Download performance summaries  

 The device connects to mobile devices via **Bluetooth** for **real-time data transfer and feedback**.

### System Components:

- **Wearable Device** *(Focus tracking & vibration feedback)*
- **Flask REST API** *(Backend server)*
- **React Native Mobile App** *(Future)*
- **Bluetooth Communication Layer**

---

## **2. User Interface Approach**

The UI focuses on **simplicity** and **user-friendly navigation**, ensuring students can easily monitor focus metrics.

 **Wireframes** were designed in **Figma** and will be converted into mobile components using **React Native libraries**.

### Planned Screens:

- **Sign In / Sign Up**: Secure user authentication  
- **Focus Dashboard**: Live attention score and activity overview  
- **Device Connection**: Bluetooth pairing & monitoring  
- **Focus History**: Past session summaries & trends  
- **Weekly Reports**: Downloadable PDFs of weekly performance  

---

## **3. Visual Design**

 **Primary Color**: `#4E73DF` *(Energetic Blue – inspires focus)*  
 **Secondary Color**: `#FFFFFF` *(Clean white background)*  
 **Font Family**: `Poppins` *(Optimized for clarity on mobile)*  

> Color and typography aim to **promote focus** and offer an **aesthetic user experience**.

---

## **4. Navigation Strategy**

EduBand uses **React Navigation** for a structured, intuitive flow:

- **Stack Navigation** → Login → Dashboard → Reports  
- **Tab Navigation** → Home, History, Settings  

---

## **5. Responsiveness Testing**

UI is validated on multiple platforms and screen sizes, including:

- 📱 iPhone 13 Pro *(iOS Simulator)*  
- 📱 Pixel 5 *(Android Emulator)*  
- 📱 Samsung Galaxy A52 *(Real Device)*  
- 📱 iPad Mini / Galaxy Tab A7 *(Small Tablets)*  

