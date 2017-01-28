

#calss header
class _UP():
	def __init__(self,): 
		self.name = "UP"
		self.definitions = [u'towards a higher position; towards a higher value, number, or level: ', u'out of the ground: ', u'from a higher to a lower position repeatedly: ', u'in or into a vertical position: ', u'in a high position; at the top: ', u'very near: ', u'to a greater degree; in order to increase: ', u'If a level or amount is up, it has increased: ', u'not in bed: ', u'to be able to get out of bed and move around again after a period of illness, because your health has improved enough', u'into existence, view, or attention: ', u'so as to be equal in quality, knowledge, or achievement: ', u'in a state of being together with other similar things: ', u'tightly or firmly in order to keep something safe or in position: ', u'broken or cut into smaller pieces; made smaller in area: ', u'to a greater age: ', u'used when talking or asking about what is happening: ', u'When a period of time is up, it is finished: ', u'into an improved position or state: ', u'to an end, finish, or state of being complete: ', u'towards the north: ', u'towards a more important place, especially a city: ', u'intended, suggested, or being considered for something: ', u'willing and able to do or take part in an activity: ', u'on trial in a court: ', u'When a road is up, it is being repaired and so is unsuitable for use: ', u"If someone's long hair is up, it is arranged on the top or back of the head: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
