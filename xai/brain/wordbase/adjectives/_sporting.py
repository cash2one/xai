

#calss header
class _SPORTING():
	def __init__(self,): 
		self.name = "SPORTING"
		self.definitions = [u'relating to sports: ', u'showing fairness and respect towards an opposing team or player']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
