

#calss header
class _DILIGENT():
	def __init__(self,): 
		self.name = "DILIGENT"
		self.definitions = [u'careful and using a lot of effort: ', u'done in a careful and detailed way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
