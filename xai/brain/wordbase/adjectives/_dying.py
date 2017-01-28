

#calss header
class _DYING():
	def __init__(self,): 
		self.name = "DYING"
		self.definitions = [u'very ill and likely to die soon: ', u'A dying tradition or industry is becoming much less common or important.', u'happening at the time someone dies, or connected with that time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
