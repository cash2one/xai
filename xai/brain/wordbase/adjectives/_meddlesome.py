

#calss header
class _MEDDLESOME():
	def __init__(self,): 
		self.name = "MEDDLESOME"
		self.definitions = [u'often getting involved in situations where you are not wanted, especially by criticizing in a damaging or annoying way']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
