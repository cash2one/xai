

#calss header
class _VIRAL():
	def __init__(self,): 
		self.name = "VIRAL"
		self.definitions = [u'caused by a virus: ', u'used to describe something that quickly becomes very popular or well known by being published on the internet or sent from person to person by email, phone, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
