fromsqlalchemyimportcreate_engine
fromsqlalchemy.ext.declarativeimportdeclarative_base
fromsqlalchemy.ormimportscoped_session,sessionmaker

fromInerukiimportPOSTGRESS_URLasDB_URI


defstart()->scoped_session:
engine=create_engine(DB_URI,client_encoding="utf8")
BASE.metadata.bind=engine
BASE.metadata.create_all(engine)
returnscoped_session(sessionmaker(bind=engine,autoflush=False))


BASE=declarative_base()
SESSION=start()
