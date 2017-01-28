

#calss header
class _INTIMATE():
	def __init__(self,): 
		self.name = "INTIMATE"
		self.definitions = [u'having, or being likely to cause, a very close friendship or personal or sexual relationship: ', u'(of knowledge or understanding) detailed, and obtained from a lot of studying or experience: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
