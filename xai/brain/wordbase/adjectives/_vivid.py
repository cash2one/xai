

#calss header
class _VIVID():
	def __init__(self,): 
		self.name = "VIVID"
		self.definitions = [u'Vivid descriptions, memories, etc. produce very clear, powerful, and detailed images in the mind: ', u'very brightly coloured: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
