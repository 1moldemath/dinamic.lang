# Requires: pip install genanki
import genanki
import os
from datetime import datetime

# -----------------------------
# Model (card type) – dark theme + larger font
# -----------------------------
MODEL_ID = 1607392319

technical_model = genanki.Model(
    MODEL_ID,
    'Technical Q&A Card',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '<div class="question">{{Question}}</div><hr><div class="answer">{{Answer}}</div>',
        },
    ],
    css=r"""
.card {
  font-family: 'Inter', sans-serif;
  font-size: 22px;
  text-align: left;
  color: #e0e0e0;
  background-color: #121212;
}
.question { color: #ffd54f; font-weight: 600; }
.answer { color: #90caf9; }
"""
)

# -----------------------------
# Deck list (subdecks)
# (Corrigi pequenos typos para nomes oficiais dos serviços)
# -----------------------------
SUBDECKS = [
    "IAM & AWS CLI",
    "EC2",
    "ELB & ASG",
    "RDS & AWS Aurora & ElastiCache",
    "Route 53",
    "VPC",
    "S3",
    "CloudFront",
    "ECS & Fargate & ECR",
    "Elastic Beanstalk",
    "CloudFormation",
    "SQS & SNS & Kinesis",
    "AWS Monitoring & CloudTrail & CloudWatch",  # "Cloud Ray" -> CloudTrail
    "Lambda",
    "API Gateway",
    "Pipelines (CodePipeline / CodeBuild / CodeDeploy)",
    "SAM (Serverless Application Model)",
    "CDK (Cloud Development Kit)",
    "Cognito",
    "Step Functions & AppSync",
    "KMS & STS & Parameter Store & Secrets Manager",
]

# -----------------------------
# Helper: unique-ish deterministic deck IDs
# -----------------------------
def deck_id_from_name(name: str) -> int:
    # Create a stable numeric ID from deck name
    base = 2059400000
    h = abs(hash(name)) % 90000
    return base + h

# -----------------------------
# Create subdecks with 1 placeholder note each
# (Anki não importa decks totalmente vazios — por isso um cartão placeholder)
# -----------------------------
def build_package():
    decks = []
    created = datetime.now().strftime("%Y-%m-%d %H:%M")

    for sub in SUBDECKS:
        full_name = f"AWS::{sub}"
        d = genanki.Deck(deck_id_from_name(full_name), full_name)

        # Placeholder note (pode deletar depois no Anki)
        note = genanki.Note(
            model=technical_model,
            fields=[
                f"[PLACEHOLDER] Add your questions here for: {sub}",
                "You can delete this example card after importing, "
                "and start adding your own Q&A flashcards for this AWS service."
            ],
            tags=["placeholder", "aws", sub.replace(" ", "_").lower()]
        )
        d.add_note(note)
        decks.append(d)

    # Cria o pacote .apkg
    output = "AWS_Deck_Structure.apkg"
    pkg = genanki.Package(decks)
    pkg.write_to_file(output)
    return os.path.abspath(output)

if __name__ == "__main__":
    path = build_package()
    print(f"Generated: {path}")
