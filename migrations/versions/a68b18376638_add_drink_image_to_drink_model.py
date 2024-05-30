"""Add drink_image to Drink model

Revision ID: a68b18376638
Revises: 
Create Date: 2024-05-30 17:28:06.941209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a68b18376638'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Update existing rows with a default value
    op.execute("UPDATE drink SET drink_image = 'default_image.jpg' WHERE drink_image IS NULL")

    with op.batch_alter_table('drink', schema=None) as batch_op:
        batch_op.alter_column('drink_image', existing_type=sa.String(length=255), nullable=False)

def downgrade():
    with op.batch_alter_table('drink', schema=None) as batch_op:
        batch_op.alter_column('drink_image', existing_type=sa.String(length=255), nullable=True)



    # ### end Alembic commands ###
