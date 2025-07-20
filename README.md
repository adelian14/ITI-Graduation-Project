# TeachFlow

*The Future of Education - AI-Powered Course Content Generation*

## 🎯 Vision

To revolutionize the way instructors design and deliver education by harnessing the power of Generative AI to create personalized, engaging, and high-quality learning experiences at scale.

## 🚀 Mission

- **Automate** the creation of complete course materials—from curriculum structure to slides and video scripts
- **Empower** instructors with AI tools that reduce content preparation time and increase teaching impact
- **Enhance** learning quality through well-structured, narrative-rich lessons tailored to different age groups and learning styles
- **Bridge** the gap between raw online content and classroom-ready resources with intelligent content transformation

## 📊 Problem Statement

### Current Challenges in Education Content Creation:

- **⏰ Time-consuming**: Searching for reliable content across the internet takes hours
- **🔄 Manual effort**: Summarizing, structuring, and designing slides is repetitive and slow
- **📉 Inconsistent quality**: Content varies between instructors and lacks standardization
- **📈 Low scalability**: Difficult to quickly adapt materials for different levels, age groups, or learning styles
- **🎥 Video creation barriers**: Requires extra skills and effort, often beyond the instructor's capacity


## ✨ Key Features

### 🗺️ Intelligent Learning Roadmap Creation
Builds adaptive roadmaps from uploaded PDFs, structuring course content into modules, lessons, and topics with hierarchical organization.

### 🌐 Language and Teaching Style Adaptation
Customizes content based on the learner's preferred language (English, Arabic, and mixed) and instructional style for a personalized experience.

### 📊 Content Extraction to PPTX
Automatically converts static PDF materials into well-structured, presentation-ready PowerPoint slides with professional formatting.

### 🎬 Narrative and Video Script Generation
Generates clear, engaging narrative text and video scripts tailored for multimedia lesson delivery and enhanced student engagement.

### Processing Pipeline:

1. **Upload Documents** → PDF files uploaded to the system
2. **Pages to Images** → Convert PDF pages to image format
3. **OCR Processor** → Extract text using Optical Character Recognition
4. **Text Patches** → Break text into manageable chunks
5. **Text Merger** → Combine and structure text coherently
6. **Content Structure** → Organize into modules, lessons, and topics
7. **JSON Converter** → Convert to structured JSON format
8. **UI Display** → Present hierarchical structure to users

## 🛠️ Technology Stack

### Core Technologies

| Technology | Purpose | Version |
|------------|---------|---------|
| **Google Gemini 2.5 Flash** | Large Language Model for content generation | Latest |
| **CrewAI** | Autonomous Agent Framework for task orchestration | Latest |
| **Google Cloud Services** | Scalable cloud infrastructure | - |
| **Firebase** | Real-time backend and database (Firestore) | Latest |
| **Flask** | Lightweight web framework for REST APIs | 2.0+ |
| **OCR Technology** | Text extraction from PDF documents | - |

### Key Technology Benefits

- **🤖 Gemini 2.5 Flash**: Fast and cost-effective understanding, summarization, and generation capabilities
- **🔄 CrewAI**: Modular orchestration of task-specific AI agents for automated workflows
- **☁️ Google Cloud**: Scalable, secure, and seamless integration with AI tools
- **🔥 Firebase**: Real-time database, authentication, and analytics support
- **⚡ Flask**: Quick REST API development and AI workflow integration

## 🚀 Getting Started

### Prerequisites

```bash
Python >= 3.8
Flask >= 2.0
Firebase Account
Google Cloud Platform Account
CrewAI Framework
OCR Libraries
```

### Installation

```bash
# Clone the repository
git clone https://github.com/adelian14/TeachFlow.git
cd TeachFlow

# Create virtual environment
python -m venv teachflow_env
source teachflow_env/bin/activate  # On Windows: teachflow_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Configure your API keys and settings in .env

# Initialize Firebase
firebase login
firebase init

# Run the application
python app.py
```

### Environment Configuration

```env
# Google AI Configuration
GOOGLE_API_KEY=your_gemini_api_key_here
GOOGLE_CLOUD_PROJECT_ID=your_project_id

# Firebase Configuration
FIREBASE_API_KEY=your_firebase_api_key
FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
FIREBASE_DATABASE_URL=https://your_project.firebaseio.com
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_STORAGE_BUCKET=your_project.appspot.com

# CrewAI Configuration
CREWAI_API_KEY=your_crewai_key

# Application Settings
FLASK_ENV=development
FLASK_DEBUG=True
UPLOAD_FOLDER=uploads/
MAX_CONTENT_LENGTH=50MB
```


## 🎯 Target Customers

### Primary Markets
1. **Independent Instructors & Trainers** - Freelance educators and corporate trainers
2. **Universities & Academic Institutions** - Higher education content creation
3. **Online Learning Platforms** - E-learning content providers
4. **Vocational Training Centers** - Professional skill development organizations
5. **Government & Educational Ministries** - Public education content standardization

## 💰 Business Model

### Revenue Streams
1. **B2C SaaS Subscriptions** - Individual instructor plans
2. **B2B Institutional Licensing** - Enterprise and academic licenses
3. **Custom AI Integration & Services** - Tailored solutions for large organizations
4. **Content Marketplace Commission** - Future feature for content sharing
5. **Assessment & Quiz Generator** - Premium add-on features

### Cost Structure
- Development and maintenance costs
- AI & Cloud infrastructure expenses
- API licensing fees (Google, CrewAI)
- Marketing and customer acquisition
- Customer support operations
- Legal compliance and data security

## 📈 SWOT Analysis

### Strengths ✅
- Solves fundamental time-saving problem in education
- Modular workflow with independent AI agents
- Multi-language support (Arabic, English, mixed)
- Comprehensive feature set (roadmaps, slides, scripts)
- Flexible teaching style customization
- Scalable SaaS architecture
- Strategic educational partnerships

### Weaknesses ⚠️
- Heavy reliance on input data quality
- No human review component
- Accuracy limitations in specialized fields
- Current processing time constraints

### Opportunities 🚀
- Rapid e-learning market growth
- LMS integration potential (Moodle, Blackboard)
- Automated assessment features
- Arabic-focused AI tool advantage
- Platform partnerships (Udemy, Coursera)

### Threats ⚡
- Competition from established AI education tools
- User concerns about AI-only content generation
- Data privacy and security requirements
- API dependency risks
- Institutional resistance to AI adoption

## 🔮 Future Roadmap

### Phase 1: Core Enhancement
- [ ] **Video Lesson Generation** - Automated video content creation
- [ ] **Automated Assessments & Quiz Generator** - Intelligent testing tools
- [ ] **Performance Optimization** - Reduce processing times
- [ ] **Quality Assurance Tools** - Content review mechanisms

### Phase 2: Content Expansion
- [ ] **Multimodal Content Integration** - Support for various media types
- [ ] **Multiple File Format Support** - Beyond PDFs (DOCX, PPTX, etc.)
- [ ] **Advanced Language Support** - Enhanced Arabic and multilingual capabilities
- [ ] **Custom Templates** - Industry-specific content templates

### Phase 3: Platform Integration
- [ ] **LMS Integrations** - Moodle, Blackboard, Canvas compatibility
- [ ] **API Marketplace** - Third-party integration ecosystem
- [ ] **Mobile Applications** - iOS and Android apps
- [ ] **Collaborative Features** - Team-based content creation

## 🔧 Current Limitations & Challenges

### Processing Performance
- **Issue**: Relatively long processing times for complex documents
- **Impact**: User experience and scalability concerns
- **Mitigation**: Ongoing optimization and infrastructure improvements

### Quality Assurance
- **Issue**: Generated content may not always align with instructor goals
- **Impact**: Manual editing often required
- **Mitigation**: Developing review mechanisms and customization options

### Language Support
- **Issue**: Currently optimized for English; Arabic support in development
- **Impact**: Limited market reach in Arabic-speaking regions
- **Mitigation**: Prioritizing Arabic language model improvements

### Cost Management
- **Issue**: Dependency on third-party LLM APIs creates recurring costs
- **Impact**: Operational expense scaling with usage
- **Mitigation**: Exploring cost optimization and alternative models


## 🔐 Security & Privacy

### Data Protection
- All uploaded documents are encrypted in transit and at rest
- User data is processed according to GDPR and educational privacy standards
- Document content is not permanently stored without user consent
- Access controls ensure institutional data privacy

### AI Ethics
- Transparent AI-generated content labeling
- Bias detection and mitigation in content generation
- Human oversight recommendations for critical educational content
- Opt-out options for data usage in model improvements


## 👥 Team Members

- **Ali Salama**: [@3lis0](https://github.com/3lis0)
- **Ali Adel**: [@adelian14](https://github.com/adelian14)
- **Alaa Hussien**: [@Alaahussen](https://github.com/Alaahussen)
- **Alaa Khaled**: [@Aalaa25](https://github.com/Aalaa25)
- **Sarah Kamel**: [@SarahNabilKamel](https://github.com/SarahNabilKamel)
- **Salma Zaher**: [@salma-zaher](https://github.com/salma-zaher)

## 📄 License

This project is licensed

---

**TeachFlow**: *Let instructors teach — and TeachFlow does the rest* 🎓🤖✨
