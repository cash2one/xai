

#calss header
class _NAVIGATIONAL():
	def __init__(self,): 
		self.name = "NAVIGATIONAL"
		self.definitions = [u'relating to the navigation of a ship, etc. or to the act of finding your way from one place to another: ', u'relating to the act of moving around a website or computer screen, or between websites or screens: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
