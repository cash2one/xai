

#calss header
class _UNSWEETENED():
	def __init__(self,): 
		self.name = "UNSWEETENED"
		self.definitions = [u'with no sugar or other sweet substances added: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
