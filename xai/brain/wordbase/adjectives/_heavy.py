

#calss header
class _HEAVY():
	def __init__(self,): 
		self.name = "HEAVY"
		self.definitions = [u'weighing a lot, and needing effort to move or lift: ', u'(especially of something unpleasant) of very or especially great force, amount, or degree: ', u'sea that is rough with large waves', u'thick, strong, solid, or strongly made: ', u'Heavy soil is thick and difficult to dig or walk through.', u'thick, solid-looking, and not delicate: ', u'Heavy machines or vehicles that are very large and powerful: ', u'used to describe something such as a situation that is dangerous or unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
