

#calss header
class _CUSTODIAL():
	def __init__(self,): 
		self.name = "CUSTODIAL"
		self.definitions = [u'a period of time that someone must stay in prison', u'relating to the legal right to care for someone or something, especially a child: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
