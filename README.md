# Currency Tracker

By: **Perry Thampiratwong**

## About the Project

This project is a lightweight currency tracking tool designed to provide users with real-time updates on the exchange rate between US dollars (USD) and Thai Baht (THB). The script fetches data from a reliable foreign exchange API and sends desktop notifications to keep users informed of the latest rates without needing to check manually.

Users can set their own notification frequency and input their API key. Note that the features available might depend on the plan you choose with the foreign exchange API. You can explore the available plans on the [FXRatesAPI](https://fxratesapi.com/pricing)

## Why I Build This Project

I built this project for several reasons:

- **For Personal Use:**
  I wanted a simple and efficient way to stay updated on the exchange rates between US dollars (USD) and Thai Baht (THB) without having to check manually every day. Automating this process saves time and ensures I always have the latest information at my fingertips.
- **Exploring API Integration:**
  I was intrigued by the idea of working with APIs and wanted to gain hands-on experience integrating them into a real-world project. This project gave me the perfect opportunity to practice retrieving and processing real-time data in a practical context.
- **Learning Experience:**
  This project helped me enhance my technical skills, including working with APIs, automating tasks, and creating a lightweight notification system.

## Getting Started

### Requirements

- [FXRatesAPI](https://fxratesapi.com/)
- [pip](https://pypi.org/project/pip/)

### Installation

1. **Clone The Repo**

```sh
  git clone https://github.com/perryjirakit/currency_tracker
```

2. **Install the necessary Python Packages**
   ```sh
   pip install -r requirements.txt
   ```
3. **Setup Your API key**

- Open the `.env.example` file in the project directory.
- Add your API key to the file:
  ```sh
  api_key=
  ```
- Save the file as `.env`.

### Setup the Notification Schedule

  #### For Window
  1. Open **Task Scheduler**
  2. Create a new Task
  3. Setup the frequency for you notification in **Triggers Tab**
  4. In **Actions Tab"
  #### For macOS
