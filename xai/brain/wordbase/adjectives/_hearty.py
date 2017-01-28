

#calss header
class _HEARTY():
	def __init__(self,): 
		self.name = "HEARTY"
		self.definitions = [u'enthusiastic, energetic, and often loudly expressed: ', u'large or (especially of food) in large amounts: ', u'very great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
