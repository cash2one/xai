

#calss header
class _RESTRICTED():
	def __init__(self,): 
		self.name = "RESTRICTED"
		self.definitions = [u'limited, especially by official rules, laws, etc.: ', u'A restricted area is one that you need official permission to enter because the police or the armed forces want to keep it secret, or because it is considered dangerous: ', u'A restricted document is one that you need official permission to read because the government wants to keep it secret.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
