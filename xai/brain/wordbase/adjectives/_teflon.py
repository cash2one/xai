

#calss header
class _TEFLON():
	def __init__(self,): 
		self.name = "TEFLON"
		self.definitions = [u'used to describe someone who manages to avoid criticism and keep a good reputation, even after they have done something wrong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
