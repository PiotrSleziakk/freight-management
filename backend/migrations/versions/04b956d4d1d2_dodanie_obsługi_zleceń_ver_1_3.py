"""Dodanie obsługi zleceń - ver 1.3

Revision ID: 04b956d4d1d2
Revises: b32ec1d90cdd
Create Date: 2024-12-04 15:37:02.365400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04b956d4d1d2'
down_revision = 'b32ec1d90cdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shipment_order', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shipment_order', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###
