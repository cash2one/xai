

#calss header
class _UNTRAINED():
	def __init__(self,): 
		self.name = "UNTRAINED"
		self.definitions = [u'never having been taught the skills for a particular job: ', u'to someone without the skill or knowledge to judge what they see: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
