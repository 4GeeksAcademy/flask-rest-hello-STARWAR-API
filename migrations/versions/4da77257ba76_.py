"""empty message

Revision ID: 4da77257ba76
Revises: d201a9e78f4f
Create Date: 2024-03-24 23:24:47.338289

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4da77257ba76'
down_revision = 'd201a9e78f4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('people_id', sa.Integer(), nullable=False))
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.create_foreign_key(None, 'people', ['people_id'], ['id'])
        batch_op.create_foreign_key(None, 'planet', ['planet_id'], ['id'])

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('src', sa.String(length=300), nullable=False))
        batch_op.add_column(sa.Column('description', sa.String(length=500), nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.drop_constraint('people_favorites_fkey', type_='foreignkey')
        batch_op.drop_column('vehicle_class')
        batch_op.drop_column('uid')
        batch_op.drop_column('manufacturer')
        batch_op.drop_column('model')
        batch_op.drop_column('cargo_capacity')
        batch_op.drop_column('lenght')
        batch_op.drop_column('favorites')
        batch_op.drop_column('max_atmosphering_speed')
        batch_op.drop_column('crew')
        batch_op.drop_column('url')
        batch_op.drop_column('consumable')
        batch_op.drop_column('cost_in_credits')

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('src', sa.String(length=500), nullable=False))
        batch_op.add_column(sa.Column('description', sa.String(length=500), nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=300),
               type_=sa.String(length=200),
               existing_nullable=False)
        batch_op.drop_constraint('planet_favorites_fkey', type_='foreignkey')
        batch_op.drop_column('uid')
        batch_op.drop_column('climate')
        batch_op.drop_column('orbital_period')
        batch_op.drop_column('manufacturer')
        batch_op.drop_column('surface_water')
        batch_op.drop_column('rotation_period')
        batch_op.drop_column('lenght')
        batch_op.drop_column('favorites')
        batch_op.drop_column('terrain')
        batch_op.drop_column('gavity')
        batch_op.drop_column('population')
        batch_op.drop_column('diameter')
        batch_op.drop_column('url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', sa.VARCHAR(length=250), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('diameter', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('population', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('gavity', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('terrain', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('favorites', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('lenght', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('rotation_period', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('surface_water', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('manufacturer', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('orbital_period', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('climate', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uid', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.create_foreign_key('planet_favorites_fkey', 'favorites', ['favorites'], ['fav_id'])
        batch_op.alter_column('name',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=300),
               existing_nullable=False)
        batch_op.drop_column('description')
        batch_op.drop_column('src')
        batch_op.drop_column('id')

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cost_in_credits', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('consumable', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('url', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('crew', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('max_atmosphering_speed', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('favorites', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('lenght', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('cargo_capacity', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('model', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('manufacturer', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('uid', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.add_column(sa.Column('vehicle_class', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('people_favorites_fkey', 'favorites', ['favorites'], ['fav_id'])
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=200),
               existing_nullable=False)
        batch_op.drop_column('description')
        batch_op.drop_column('src')
        batch_op.drop_column('id')

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.drop_column('people_id')
        batch_op.drop_column('planet_id')

    # ### end Alembic commands ###
