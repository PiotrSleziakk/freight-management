"""Zwiększenie długości kolumny passwor

Revision ID: b32ec1d90cdd
Revises: 18d326160e58
Create Date: 2024-12-03 16:07:16.381562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b32ec1d90cdd'
down_revision = '18d326160e58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shipment_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_number', sa.String(length=100), nullable=False),
    sa.Column('sender', sa.String(length=200), nullable=False),
    sa.Column('recipient', sa.String(length=200), nullable=False),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shipment_order')
    # ### end Alembic commands ###
