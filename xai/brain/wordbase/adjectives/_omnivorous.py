

#calss header
class _OMNIVOROUS():
	def __init__(self,): 
		self.name = "OMNIVOROUS"
		self.definitions = [u'naturally able to eat both plants and meat: ', u'enthusiastic and interested in many different areas of a subject: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
