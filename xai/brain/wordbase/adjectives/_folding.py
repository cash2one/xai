

#calss header
class _FOLDING():
	def __init__(self,): 
		self.name = "FOLDING"
		self.definitions = [u'A folding chair, bed, bicycle, etc. can be folded into a smaller size to make it easier to store or carry.', u'A folding door is made of several parts joined together that can be folded against each other when the door is opened.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
