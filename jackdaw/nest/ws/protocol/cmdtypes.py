import enum

class NestOpCmd(enum.Enum):
	GATHER = 'GATHER'
	KERBEROAST = 'KERBEROAST'
	KERBEROASTRES = 'KERBEROASTRES'
	ASREPROAST = 'ASREPROAST'
	ASREPROASTRES = 'ASREPROASTRES'
	KERBEROSTGS = 'KERBEROSTGS'
	KERBEROSTGSRES = 'KERBEROSTGSRES'
	KERBEROSTGT = 'KERBEROSTGT'
	KERBEROSTGTRES = 'KERBEROSTGTRES'
	SMBSESSIONS = 'SMBSESSIONS'
	SMBFILES = 'SMBFILES'
	SMBDCSYNC = 'SMBDCSYNC'
	PATHSHORTEST = 'PATHSHORTEST'
	PATHDA = 'PATHDA'
	GETOBJINFO = 'GETOBJINFO'
	CHANGEAD = 'CHANGEAD'
	LISTADS = 'LISTADS'
	LISTADSRES = 'LISTADSRES'

	OK = 'OK'
	ERR = 'ERR'
	LOG = 'LOG'
	CANCEL = 'CANCEL'
	
	TCPSCAN = 'TCPSCAN'
	TCPSCANRES = 'TCPSCANRES'
	
	PATHRES = 'PATHRES'
	GATHERSTATUS = 'GATHERSTATUS'
	USERRES = 'USERRES'
	COMPUTERRES = 'COMPUTERRES'
	SMBSESSIONRES = 'SMBSESSIONRES'
	SMBSHARERES	= 'SMBSHARERES'
	SMBLOCALGROUPRES = 'SMBLOCALGROUPRES'
	LOADAD = 'LOADAD'
	GROUPRES = 'GROUPRES'
	EDGERES = 'EDGERES'
	EDGEBUFFRES = 'EDGEBUFFRES'
	USERBUFFRES = 'USERBUFFRES'
	GROUPBUFFRES = 'GROUPBUFFRES'
	COMPUTERBUFFRES = 'COMPUTERBUFFRES'
	SMBSHAREBUFFRES = 'SMBSHAREBUFFRES'
	SMBFILERES = 'SMBFILERES'

	ADDCRED = 'ADDCRED'
	LISTCRED = 'LISTCRED'
	GETCRED = 'GETCRED'
	CREDRES = 'CREDRES'

	ADDTARGET = 'ADDTARGET'
	LISTTARGET = 'LISTTARGET'
	GETTARGET = 'GETTARGET'
	TARGETRES = 'TARGETRES'

	LISTGRAPHS = 'LISTGRAPHS'
	CHANGEGRAPH = 'CHANGEGRAPH'
	LOADGRAPH = 'LOADGRAPH'
	LISTGRAPHRES = 'LISTGRAPHRES'
	
	LISTAGENTS = 'LISTAGENTS'
	AGENT = 'AGENT'

	OBJOWNED = 'OBJOWNED'
	OBJHVT = 'OBJHVT'


	WSNETROUTERCONNECT = 'WSNETROUTERCONNECT'
	WSNETROUTERDISCONNECT = 'WSNETROUTERDISCONNECT'
	NOTIFY = 'NOTIFY'
	WSNETROUTER = 'WSNETROUTER'
	WSNETLISTROUTERS = 'WSNETLISTROUTERS'


	PATHKERB = 'PATHKERB'
	PATHASREP = 'PATHASREP'
	PATHOWNED = 'PATHOWNED'

	RDPCONNECT = 'RDPCONNECT'
	RDPRECT = 'RDPRECT'
	RDPMOUSE = 'RDPMOUSE'

	LDAPSPNS = 'LDAPSPNS'