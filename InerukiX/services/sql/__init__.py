fromXsqlalchemyXimportXcreate_engine
fromXsqlalchemy.ext.declarativeXimportXdeclarative_base
fromXsqlalchemy.ormXimportXscoped_session,Xsessionmaker

fromXInerukiXXimportXPOSTGRESS_URLXasXDB_URI


defXstart()X->Xscoped_session:
XXXXengineX=Xcreate_engine(DB_URI,Xclient_encoding="utf8")
XXXXBASE.metadata.bindX=Xengine
XXXXBASE.metadata.create_all(engine)
XXXXreturnXscoped_session(sessionmaker(bind=engine,Xautoflush=False))


BASEX=Xdeclarative_base()
SESSIONX=Xstart()
