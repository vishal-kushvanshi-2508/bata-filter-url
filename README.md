# 👟 Bata Filter URL Data Extraction

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Web Scraping](https://img.shields.io/badge/Web-Scraping-green?style=for-the-badge)
![URL Filtering](https://img.shields.io/badge/Filter-URL%20Generation-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)

A Python-based data extraction project designed to generate and process filtered product URLs from Bata's online catalog. The project automates URL generation, product discovery, and structured data collection, demonstrating real-world web scraping and data engineering concepts.

---

## 📖 Overview

Bata Filter URL is a Python automation project that works with filtered product URLs to collect structured product information from an e-commerce platform.

The project performs an end-to-end workflow:

* Generates filtered URLs
* Sends HTTP requests
* Retrieves product listing pages
* Extracts product information
* Processes and validates collected data
* Stores structured output for analysis

This project demonstrates practical implementation of:

* URL Parameter Handling
* Web Scraping
* Data Extraction Pipelines
* HTML Parsing
* E-commerce Data Collection
* Python Automation

---

## 🎯 Why This Project?

The goal of this project was to gain hands-on experience with e-commerce scraping workflows and dynamic URL generation techniques.

Key learning objectives include:

* Working with filter-based URLs
* Extracting structured product data
* Understanding e-commerce page structures
* Building scalable scraping workflows
* Data validation and processing

---

## 🚀 Key Features

* Filter URL generation

* Automated product discovery

* Product listing extraction

* Structured data collection

* Data cleaning and validation

* Modular architecture

* Scalable workflow design

* Easy maintenance and extension

---

## 🛠️ Technologies Used

| Technology     | Purpose                   |
| -------------- | ------------------------- |
| Python         | Core Programming Language |
| Requests       | HTTP Requests             |
| BeautifulSoup4 | HTML Parsing              |
| JSON           | Data Serialization        |
| Logging        | Monitoring & Debugging    |

---

## 📊 Extracted Data

Depending on the target pages, the scraper can collect:

* Product Name
* Product Price
* Product Brand
* Product Category
* Product URL
* Product Availability
* Product Description
* Product Rating
* Filter Information

---

## 🏗️ Project Architecture

```text
Bata Website
      │
      ▼
Filter URL Generation
      │
      ▼
HTTP Requests
      │
      ▼
Product Listings
      │
      ▼
Data Extraction
      │
      ▼
Data Validation
      │
      ▼
Structured Output
```

---

## 🔄 Workflow

```text
1. Generate Filter URLs
            │
            ▼
2. Send Requests
            │
            ▼
3. Download Product Pages
            │
            ▼
4. Extract Product Data
            │
            ▼
5. Validate Information
            │
            ▼
6. Save Structured Output
```

---

## 📁 Project Structure

```text
bata-filter-url/
│
├── main.py
├── requirements.txt
├── README.md
├── output/
├── logs/
└── .gitignore
```

### Module Description

#### main.py

Project entry point that manages the complete scraping workflow.

#### output/

Stores extracted product data.

#### logs/

Contains execution logs and debugging information.

#### requirements.txt

Lists all required Python dependencies.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/vishal-kushvanshi-2508/bata-filter-url.git
```

### Navigate to Project Directory

```bash
cd bata-filter-url
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Execute:

```bash
python main.py
```

The scraper will automatically:

1. Generate filtered URLs
2. Retrieve product pages
3. Extract product information
4. Process and validate data
5. Save structured output

---

## 📂 Example Output

```json
{
    "product_name": "Men Casual Shoes",
    "brand": "Bata",
    "price": "1999",
    "category": "Footwear",
    "availability": "In Stock",
    "product_url": "https://..."
}
```

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

* URL Parameter Management
* Web Scraping Fundamentals
* HTTP Request Handling
* HTML Parsing
* E-commerce Data Extraction
* Data Cleaning & Validation
* Python Automation
* Structured Data Processing

---

## 🔮 Future Improvements

* Multi-threaded scraping
* Async request handling
* Database integration
* CSV & Excel export
* Docker containerization
* REST API support
* Automated scheduling
* Data visualization dashboard

---

## 👨‍💻 Author

### Vishal Kushvanshi

#### GitHub Profiles

🔹 Professional Portfolio

https://github.com/vishal-kushvanshi-2508

🔹 Practice Projects & Learning

https://github.com/vishal-2508

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

