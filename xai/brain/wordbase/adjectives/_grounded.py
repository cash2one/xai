

#calss header
class _GROUNDED():
	def __init__(self,): 
		self.name = "GROUNDED"
		self.definitions = [u'Someone who is grounded makes good decisions and does not say or do stupid things: ', u'used to describe an aircraft that is prevented from flying for some reason, or a ship that cannot move because it has hit solid ground', u'A child or young person who is grounded is not allowed to go out as a punishment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
