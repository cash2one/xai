

#calss header
class _BUSY():
	def __init__(self,): 
		self.name = "BUSY"
		self.definitions = [u'If you are busy, you are working hard, or giving your attention to a particular thing: ', u'A busy place is full of activity or people: ', u'In a busy period, you have a lot of things to do: ', u'If a phone line is busy, someone is using it: ', u'having too much decoration or too many colours: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
