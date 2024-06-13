"""baseline

Revision ID: initial
Revises: 
Create Date: 2024-06-13 16:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Since the table already exists, we can just pass here
    pass

def downgrade():
    # Dropping the table if needed in the future
    op.drop_table('user')
