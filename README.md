# Plant Disease Suggestion

This repository contains a **Plant Disease Suggestion** system designed to assist in the identification and management of plant diseases. By analyzing images of plant leaves, the system provides accurate diagnoses and suggests appropriate treatments, aiming to support farmers and gardeners in maintaining healthy crops.

## Features

- **Image Analysis**: Utilizes machine learning algorithms to detect and classify plant diseases from leaf images.
- **Disease Database**: Offers detailed information on various plant diseases, including symptoms and preventive measures.
- **Treatment Recommendations**: Suggests effective treatments and management practices for identified diseases.

## Technologies Used

- **Backend**: Python
- **Machine Learning**: TensorFlow, Keras
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite3

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Chaaivisva/Plant-Disease-Suggestion.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd Plant-Disease-Suggestion
   ```
3. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```
6. **Run the Application**:
   ```bash
   python manage.py runserver
   ```

## Usage

- **Access the Application**: Open your web browser and navigate to `http://127.0.0.1:8000/`.
- **Upload Leaf Image**: Use the interface to upload an image of the affected plant leaf.
- **View Diagnosis**: Receive the analysis results, including the disease name and treatment suggestions.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the MIT License.

## Acknowledgements

Special thanks to all contributors and the open-source community for their support.

